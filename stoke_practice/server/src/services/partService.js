// services/partService.ts
import { PrismaClient } from '@prisma/client';
const prisma = new PrismaClient();

// SCENARIO 1: Complex Creation (Transactional)
// Creating an Engine AND its Sub-components in one atomic move.
export const createAssembly = async (data) => {
  // logic: validating serial numbers could go here
  
  return await prisma.part.create({
    data: {
      name: data.name,
      serialNumber: data.serialNumber,
      status: 'ASSEMBLY_IN_PROGRESS',
      children: {
        create: data.children.map(child => ({
            name: child.name,
            serialNumber: child.serialNumber,
            status: 'PENDING'
        }))
      }
    },
    include: { children: true } // Return the full tree
  });
};

// SCENARIO 2: Smart Update (The "Boltline" Logic)
// Adding a test result and updating the Part status automatically.
export const addTestResult = async (partId, testData) => {
  return await prisma.$transaction(async (tx) => {
    // 1. Create the Test Record (Audit Log)
    const testResult = await tx.testResult.create({
      data: {
        type: testData.type,
        result: testData.result,
        partId: partId
      }
    });

    // 2. Determine new status logic
    // If the test FAILED, the Part status is now FAIL.
    // If it PASSED, we might leave it or move it to READY.
    let newStatus = undefined;
    if (testData.result === 'FAIL') {
      newStatus = 'FAIL';
    }

    // 3. Update the Part ONLY if status changed
    if (newStatus) {
      await tx.part.update({
        where: { id: partId },
        data: { status: newStatus }
      });
    }

    return testResult;
  });
};
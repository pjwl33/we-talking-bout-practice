// partController.js aka server.js
const express = require('express');
const { PrismaClient } = require('@prisma/client');
const cors = require('cors');

const prisma = new PrismaClient();
const app = express();

// Middleware to parse JSON bodies (CRITICAL for POST/PATCH)
app.use(express.json());
app.use(cors());


// // POST /api/parts
// // Payload: { name: "Engine", serialNumber: "SN1", children: [...] }
// router.post('/parts', async (req, res) => {
//   try {
//     const assembly = await createAssembly(req.body);
//     res.status(201).json(assembly);
//   } catch (error) {
//     // Senior Dev Tip: distinct error codes for unique constraint violations
//     if (error.code === 'P2002') {
//       return res.status(409).json({ error: "Serial Number already exists" });
//     }
//     res.status(500).json({ error: "Failed to create assembly" });
//   }
// });

// // POST /api/parts/:id/tests
// // Payload: { type: "Pressure Test", result: "FAIL" }
// router.post('/parts/:id/tests', async (req, res) => {
//   try {
//     const result = await addTestResult(req.params.id, req.body);
//     res.status(201).json(result);
//   } catch (error) {
//     res.status(500).json({ error: "Failed to record test result" });
//   }
// });

// export default router;

// GET /api/parts
// const allParts = await prisma.part.findMany();
app.get('/api/parts', async (req, res) => {

  const allParts = await prisma.part.findMany();
  // 2. Simulate Network Latency (Critical for showing loading states in UI)
  setTimeout(() => {
    res.json(allParts);
  }, 800); 
});

// GET /api/parts/:id
app.get('/api/parts/:id', (req, res) => {
  const { id } = req.params;

  // 1. Simulate Database Lookup
  // In a real scenario, this would be: await prisma.part.findUnique(...)
  if (id !== 'eng-nova-001') {
    return res.status(404).json({ error: 'Part not found' });
  }

  // 2. Simulate Network Latency (Critical for showing loading states in UI)
  setTimeout(() => {
    res.json(mockData);
  }, 800); 
});

// ---------------------------------------------------------
// 1. CREATE: Add a new Part (with optional Children)
// ---------------------------------------------------------
app.post('/api/parts', async (req, res) => {
  const { name, serialNumber, parentId, children } = req.body;

  // Basic Validation
  if (!name || !serialNumber) {
    return res.status(400).json({ error: 'Name and Serial Number are required' });
  }

  try {
    const newPart = await prisma.part.create({
      data: {
        name,
        serialNumber,
        status: 'PENDING', // Default status
        parentId: parentId || null, // Optional: Link to a parent assembly
        
        // Advanced: Create sub-components in the same request (Nested Write)
        children: children?.length > 0 ? {
          create: children.map(child => ({
            name: child.name,
            serialNumber: child.serialNumber,
            status: 'PENDING'
          }))
        } : undefined
      },
      include: { children: true } // Return the created structure
    });

    res.status(201).json(newPart); // 201 = Created
  } catch (error) {
    // Handle Unique Constraint Violation (P2002 is Prisma's error code)
    if (error.code === 'P2002') {
      return res.status(409).json({ error: 'Part with this Serial Number already exists' });
    }
    console.error(error);
    res.status(500).json({ error: 'Failed to create part' });
  }
});

// ---------------------------------------------------------
// 2. UPDATE: Modify a Part (Status, Name, or Move it)
// ---------------------------------------------------------
app.patch('/api/parts/:id', async (req, res) => {
  const { id } = req.params;
  const { status, name, parentId } = req.body;

  try {
    const updatedPart = await prisma.part.update({
      where: { id },
      data: {
        // Only update fields that are provided in the body
        ...(status && { status }),
        ...(name && { name }),
        ...(parentId !== undefined && { parentId }) // Allow moving a part to a new assembly
      }
    });

    res.json(updatedPart);
  } catch (error) {
    if (error.code === 'P2025') {
      return res.status(404).json({ error: 'Part not found' });
    }
    res.status(500).json({ error: 'Failed to update part' });
  }
});

// ---------------------------------------------------------
// 3. DELETE: Remove a Part
// ---------------------------------------------------------
app.delete('/api/parts/:id', async (req, res) => {
  const { id } = req.params;

  try {
    // AEROSPACE LOGIC: "Protective Delete"
    // Check if this part has children before deleting. 
    // You don't want to accidentally delete an Engine and orphan its Valves.
    const partToCheck = await prisma.part.findUnique({
      where: { id },
      include: { children: true }
    });

    if (!partToCheck) {
      return res.status(404).json({ error: 'Part not found' });
    }

    if (partToCheck.children.length > 0) {
      return res.status(400).json({ 
        error: 'Cannot delete an assembly that still contains sub-components. Remove children first.' 
      });
    }

    // Proceed with delete
    await prisma.part.delete({
      where: { id }
    });

    res.status(204).send(); // 204 = No Content (Successful delete)
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Failed to delete part' });
  }
});

const PORT = 3001;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// In-Memory Mock Database
// let partsDB = []; 

// // Mock POST
// app.post('/api/parts', (req, res) => {
//   const newPart = { id: Date.now().toString(), ...req.body, children: [] };
//   partsDB.push(newPart);
//   res.status(201).json(newPart);
// });

// // Mock DELETE
// app.delete('/api/parts/:id', (req, res) => {
//   partsDB = partsDB.filter(p => p.id !== req.params.id);
//   res.status(204).send();
// });
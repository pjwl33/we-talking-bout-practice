// utils/partUtils.js
export const isSystemCompromised = (part) => {
  // Logic: A system is compromised if it or ANY of its children have failed.
  if (part.status === 'FAIL') return true;
  if (part.children) {
    return part.children.some(child => isSystemCompromised(child));
  }
  return false;
};

// __tests__/partUtils.test.js
import { isSystemCompromised } from '../utils/partUtils';

describe('Traceability Logic', () => {
  test('returns false for a healthy system', () => {
    const healthyPart = { status: 'PASS', children: [{ status: 'PASS' }] };
    expect(isSystemCompromised(healthyPart)).toBe(false);
  });

  test('returns true if a deep sub-component has failed', () => {
    // Boltline Scenario: The main engine is "Pending", but a nozzle inside has failed.
    const compromisedPart = { 
      status: 'PENDING', 
      children: [
        { status: 'PASS' },
        { status: 'FAIL' } // The failure vector
      ] 
    };
    expect(isSystemCompromised(compromisedPart)).toBe(true);
  });
});
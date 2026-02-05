// PartDashboard.tsx
import React, { useState, useEffect } from 'react';

// Types enforce contract between API and UI
interface TestResult {
  id: string;
  type: string;
  result: 'PASS' | 'FAIL';
  date: string;
}

interface Part {
  id: string;
  name: string;
  serialNumber: string;
  status: string;
  tests: TestResult[];
  children?: Part[]; // Recursive type for sub-assemblies
}

const StatusBadge = ({ status }: { status: string }) => {
  const color = status === 'FAIL' ? 'bg-red-500' : status === 'PASS' ? 'bg-green-500' : 'bg-yellow-500';
  return <span className={`px-2 py-1 rounded text-white text-xs ${color}`}>{status}</span>;
};

export default function PartDashboard({ partId }: { partId: string }) {
  const [part, setPart] = useState<Part | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchPart = async () => {
      try {
        setLoading(true);
        const response = await fetch(`http://localhost:3001/api/parts/${partId}`);
        
        if (!response.ok) throw new Error('Failed to fetch part genealogy');
        
        const data = await response.json();
        setPart(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error');
      } finally {
        setLoading(false);
      }
    };

    fetchPart();
  }, [partId]);

  if (loading) return <div>Loading Traceability Data...</div>;
  if (error) return <div className="text-red-600">Error: {error}</div>;
  if (!part) return null;

  return (
    <div className="p-6 border rounded shadow-md max-w-2xl">
      {/* Header Section */}
      <div className="flex justify-between items-center mb-4">
        <div>
          <h1 className="text-xl font-bold">{part.name}</h1>
          <p className="text-gray-500 text-sm">SN: {part.serialNumber}</p>
        </div>
        <StatusBadge status={part.status} />
      </div>

      {/* Audit Trail Section */}
      <div className="mb-6">
        <h3 className="font-semibold border-b mb-2">Recent Test History</h3>
        <ul className="space-y-1">
          {part.tests.map((test) => (
            <li key={test.id} className="flex justify-between text-sm">
              <span>{test.type}</span>
              <span className={test.result === 'FAIL' ? 'text-red-600 font-bold' : 'text-green-600'}>
                {test.result}
              </span>
            </li>
          ))}
        </ul>
      </div>

      {/* Recursive Sub-Components Section */}
      {part.children && part.children.length > 0 && (
        <div>
          <h3 className="font-semibold border-b mb-2">Sub-Components (BOM)</h3>
          <div className="pl-4 border-l-2 border-gray-200">
            {part.children.map((child) => (
              <div key={child.id} className="mb-2 flex justify-between items-center">
                <span>{child.name}</span>
                <StatusBadge status={child.status} />
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
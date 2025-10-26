import axios from 'axios';

export interface OptimizePayload {
  site: string;
  sport: string;
  roster: Record<string, number>;
  salary_cap: number;
  players: any[];
  constraints: any;
  objective: string;
}

export const runOptimization = async (payload: OptimizePayload) => {
  const response = await axios.post('http://localhost:8000/optimize', payload);
  return response.data;
};

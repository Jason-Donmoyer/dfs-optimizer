export type Sport = { id: string; name: string; slates: Slate[] };
export type Slate = { id: string; name: string; site: string; sport: string };

export const getSports = async (): Promise<Sport[]> => {
  // Example static data; replace with DB fetch
  return [
    { id: 'nfl', name: 'NFL', slates: [{ id: 'main', name: 'Main', site: 'DK', sport: 'nfl' }] },
    { id: 'nba', name: 'NBA', slates: [] },
  ];
};

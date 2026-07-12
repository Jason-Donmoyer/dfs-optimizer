interface Player {
  name: string;
  slot: string;
  salary: number;
  projection: number;
}

interface LineupSuccess {
  lineup: Player[];
}

interface LineupError {
  detail: string;
}

type LineupResponse = LineupSuccess | LineupError;

async function getLineup(): Promise<LineupSuccess> {
  const res = await fetch("http://localhost:8000/lineup?sport=NFL&site=DraftKings", {
    cache: "no-store"
  });
  if (res.ok) {
    return res.json() as Promise<LineupSuccess>;
  } else {
    const errorData = await res.json();
    throw new Error(errorData.detail);
  }
}

export default async function Home() {
  const data = await getLineup();

  return (
    <main style={{ padding: "2rem" }}>
      <h1>DFS Lineup</h1>
      <ul>
        {data.lineup.map((player: Player, i: number) => (
          <li key={i}>
            {player.name} - {player.slot} - ${player.salary}
          </li>
        ))}
      </ul>
    </main>
  );
}
async function getLineup() {
  const res = await fetch("http://localhost:8000/lineup?sport=NFL&site=DraftKings", {
    cache: "no-store"
  });
  return res.json();
}

export default async function Home() {
  const data = await getLineup();

  return (
    <main style={{ padding: "2rem" }}>
      <h1>DFS Lineup</h1>
      <ul>
        {data.lineup.map((player: any, i: number) => (
          <li key={i}>
            {player.name} - {player.slot} - ${player.salary}
          </li>
        ))}
      </ul>
    </main>
  );
}
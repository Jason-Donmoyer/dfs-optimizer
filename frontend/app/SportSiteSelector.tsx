"use client";

import { useRouter, useSearchParams } from "next/navigation";

export default function SportSiteSelector() {
    const router = useRouter();
    const searchParams = useSearchParams();

    const sport = searchParams.get("sport") ?? "NFL";
    const site = searchParams.get("site") ?? "DraftKings";

    function updateParams(newSport: string, newSite: string) {
        router.push(`/?sport=${newSport}&site=${newSite}`);
    }

    return (
        <div>
            <select value={sport} onChange={(e) => updateParams(e.target.value, site)}>
                <option value="NFL">NFL</option>
                <option value="NBA">NBA</option>
                <option value="MLB">MLB</option>
                <option value="NHL">NHL</option>
                <option value="CFB">CFB</option>
                <option value="PGA">PGA</option>
            </select>

            <select value={site} onChange={(e) => updateParams(sport, e.target.value)}>
                <option value="DraftKings">DraftKings</option>
                <option value="Fanduel">fanDuel</option>
            </select>
        </div>
    );
}
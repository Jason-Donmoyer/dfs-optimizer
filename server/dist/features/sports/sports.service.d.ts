export type Sport = {
    id: string;
    name: string;
    slates: Slate[];
};
export type Slate = {
    id: string;
    name: string;
    site: string;
    sport: string;
};
export declare const getSports: () => Promise<Sport[]>;
//# sourceMappingURL=sports.service.d.ts.map
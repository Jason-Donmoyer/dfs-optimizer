import { getSports } from './sports.service';
export const getSportsHandler = async (_request, reply) => {
    const sports = await getSports();
    reply.send(sports);
};
//# sourceMappingURL=sports.controller.js.map
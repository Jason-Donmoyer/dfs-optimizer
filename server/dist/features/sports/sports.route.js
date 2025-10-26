import { getSportsHandler } from './sports.controller';
async function sportsRoutes(fastify) {
    fastify.get('/sports', { schema: {} }, getSportsHandler);
}
export default sportsRoutes;
//# sourceMappingURL=sports.route.js.map
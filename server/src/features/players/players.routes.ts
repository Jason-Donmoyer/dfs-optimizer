import type { FastifyInstance } from 'fastify';
import { getPlayersHandler } from './players.controller';

async function playersRoutes(fastify: FastifyInstance) {
  fastify.get('/slates/:site/:sport/:id/players', { schema: {} }, getPlayersHandler);
}

export default playersRoutes;

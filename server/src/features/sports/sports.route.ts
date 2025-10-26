import type { FastifyInstance } from 'fastify';
import { getSportsHandler } from './sports.controller';

async function sportsRoutes(fastify: FastifyInstance) {
  fastify.get('/sports', { schema: {} }, getSportsHandler);
}

export default sportsRoutes;

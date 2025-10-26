import type { FastifyInstance } from 'fastify';
import { optimizeHandler } from './optimize.controller';

async function optimizeRoutes(fastify: FastifyInstance) {
  fastify.post('/optimize', { schema: {} }, optimizeHandler);
}

export default optimizeRoutes;

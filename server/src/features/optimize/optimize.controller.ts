import type { FastifyRequest, FastifyReply } from 'fastify';
import { z } from 'zod';
import { runOptimization } from './optimize.service';

const optimizeSchema = z.object({
  site: z.string(),
  sport: z.string(),
  roster: z.record(z.string(), z.number()),
  salary_cap: z.number(),
  players: z.array(z.any()),
  constraints: z.any(),
  objective: z.string(),
});

export const optimizeHandler = async (request: FastifyRequest, reply: FastifyReply) => {
  const body = optimizeSchema.parse(request.body);
  const result = await runOptimization(body);
  reply.send(result);
};

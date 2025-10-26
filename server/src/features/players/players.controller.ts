import type { FastifyRequest, FastifyReply } from 'fastify';
import { z } from 'zod';
import { getPlayers } from './players.service';

const paramsSchema = z.object({
  site: z.string().toUpperCase(),
  sport: z.string().toLowerCase(),
  id: z.string(),
});

export const getPlayersHandler = async (request: FastifyRequest, reply: FastifyReply) => {
  const { site, sport, id } = paramsSchema.parse(request.params);
  const players = await getPlayers(site, sport, id);
  reply.send(players);
};

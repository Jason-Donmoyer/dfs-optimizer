import type { FastifyRequest, FastifyReply } from 'fastify';
import { getSports } from './sports.service';

export const getSportsHandler = async (_request: FastifyRequest, reply: FastifyReply) => {
  const sports = await getSports();
  reply.send(sports);
};

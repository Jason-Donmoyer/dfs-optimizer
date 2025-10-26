import type { ZodType } from 'zod';
import { ZodError } from 'zod';
import type { FastifyRequest, FastifyReply } from 'fastify';

export const validate = (schema: ZodType) => async (request: FastifyRequest, reply: FastifyReply) => {
  try {
    schema.parse(request.body);
  } catch (err) {
    if (err instanceof ZodError) {
      reply.status(400).send({ errors: err.issues });
      return;
    }
    throw err;
  }
};
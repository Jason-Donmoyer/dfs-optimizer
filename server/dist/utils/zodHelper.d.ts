import type { ZodType } from 'zod';
import type { FastifyRequest, FastifyReply } from 'fastify';
export declare const validate: (schema: ZodType) => (request: FastifyRequest, reply: FastifyReply) => Promise<void>;
//# sourceMappingURL=zodHelper.d.ts.map
import { ZodError } from 'zod';
export const validate = (schema) => async (request, reply) => {
    try {
        schema.parse(request.body);
    }
    catch (err) {
        if (err instanceof ZodError) {
            reply.status(400).send({ errors: err.issues });
            return;
        }
        throw err;
    }
};
//# sourceMappingURL=zodHelper.js.map
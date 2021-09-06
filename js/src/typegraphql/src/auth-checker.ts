import { AuthChecker } from 'type-graphql';

export function authChecker(
    { context: { user } },
    roles,
) {
    // Only check if user exists.
    if (roles.length === 0) {
        return user !== undefined;
    }

    // If no user, restrict access.
    if (!user) {
        return false;
    }
    if (user.roles.some(role => roles.includes(role))) {
        // grant access if the roles overlap.
        return true;
    }

    // no roles matched, restrict access
    return false
}
// This example uses Next.js with React Server Components.
import { WorkOS } from '@workos-inc/node';

const workos = new WorkOS(process.env.WORKOS_API_KEY);
const clientId = process.env.WORKOS_CLIENT_ID;

export function getAuthorizationUrl() {
  const authorizationUrl = workos.userManagement.getAuthorizationUrl({
    // Specify that we'd like AuthKit to handle the authentication flow
    provider: 'authkit',

    // The callback endpoint that WorkOS will redirect to after a user authenticates
    redirectUri: 'http://localhost:3000/callback',
    clientId,
  });

  return authorizationUrl;
}

/*
  Because RSC allows running code on the server, you can
  call `getAuthorizationUrl()` directly within a server component:

  function SignInButton() {
    const authorizationUrl = getAuthorizationUrl();
    return <a href={authorizationUrl}>Sign In</a>;
  }
*/

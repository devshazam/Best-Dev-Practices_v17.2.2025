// 'use client';

import { getSession } from "@auth0/nextjs-auth0";
import ZustandProvider from "@/providers/auth-zustand/ZustandProvider";

export default async function UserStoreProvider() {
  const session = await getSession();
  const user = session?.user;

  return (
    <>
      <ZustandProvider user={user} >
        <></>
      </ZustandProvider>
  </>
  );
}

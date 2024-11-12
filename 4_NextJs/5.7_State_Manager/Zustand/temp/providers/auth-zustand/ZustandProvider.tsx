'use client'
import React, { useEffect } from 'react'
import { useUserStore } from '@/stores'
import { TUser } from '@/x-types';


export default function ZustandProvider({ user, children }: { user: TUser | undefined; children: React.ReactNode; }) {

  const { login } = useUserStore()

  useEffect(() => {
    if(!user) return;
    login(user)
  }, [user])

  return children
}
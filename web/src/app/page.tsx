"use server"

import { Button } from "@/components/ui/button";
import Link from "next/link";


export default function Home() {
  async function retrieveWorkOSURL() {
    const res = await fetch('{process.env.NEXT_PUBLIC_API_URL}/auth/login')

    if (!res.ok) {
      throw new Error('Failed to fetch login url')
    }

    return res.json()
  };


  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">

      <Button asChild>
        <Link href={retrieveWorkOSURL}>Login</Link>
      </Button>
    </main>
  )
}

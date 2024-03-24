"use client"
import { useState, useEffect } from 'react';
import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function Home() {
  const [url, setUrl] = useState('');

  useEffect(() => {
    async function retrieveWorkOSURL() {
      const url = `${process.env.NEXT_PUBLIC_API_URL}/auth/login`;
      console.log('URL:', url);

      const res = await fetch(url);

      if (!res.ok) {
        throw new Error('Failed to fetch login url');
      }

      const data = await res.json();
      setUrl(data.url);
    }

    retrieveWorkOSURL();
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <Button asChild>
        <Link href={url}>Login</Link>
      </Button>
    </main>
  );
}

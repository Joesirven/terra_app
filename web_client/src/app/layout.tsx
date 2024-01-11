import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import FloatingNavbar from '@/components/FloatingNavbar'
import Navbar from '@/components/NavBar'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Terra World',
  description: 'the green school, but online',

}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Navbar />
        <FloatingNavbar />
        {children}
      </body>
    </html>
  )
}

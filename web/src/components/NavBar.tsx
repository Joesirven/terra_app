"use client"
import React from 'react'
import Logo from './Logo'
import Link from 'next/link'
import { Menu } from 'lucide-react';

// a burger navbar for mobile that hides on desktop and on click opens a menu

    // the menu has links to the different pages
    // the menu has a link to the login page
    // the menu has a link to the add your school page
    // the menu has a link to the about page

function Navbar() {
    const [isOpen, setIsOpen] = React.useState(false);
    const toggle = () => setIsOpen(!isOpen);




  return (
    <div className='flex justify-between items-center p-4 z-[10] text-center ml-auto mr-auto relative'>
        <div className='w-4'>
            <Link href="/" className='w-4'>
                <Logo />
            </Link>
            {isOpen ? <p>open</p> : <p>close</p> }
        </div>
        <div>
        <div className="relative">
            <Menu onClick={toggle}/>

            {isOpen ? (
                <div className="w-full overflow-hidden z-[100] absolute top-full left-0">
                    <div className="box-border text-center bg-gray-800 flex flex-col items-start overflow-visible p-5 translate-y-0 translate-x-0 transition-transform duration-400 ease-linear w-full">
                        <Link href="#hero" className="text-white p-4 font-bold rounded-full bg-zinc-800 hover:bg-white hover:text-black transition-colors cursor-pointer pb-4 duration-200 w-full text-left">
                            Home
                        </Link>
                        <Link href="#about" className="text-white p-4 font-bold rounded-full hover:bg-white hover:text-black transition-colors w-full text-left">
                            About
                        </Link>
                        <Link href="/auth/" className="text-white p-4 font-bold rounded-full hover:bg-white hover:text-black transition-colors w-full text-left">
                            Add Your School
                        </Link>
                        <Link href="/auth/login" className="text-white p-4 font-bold rounded-full bg-zinc-800 hover:bg-white hover:text-black transition-colors w-full text-left">
                            Login
                        </Link>
                    </div>
                </div>
            ) : null}
</div>




        </div>



    </div>
  )
}

export default Navbar

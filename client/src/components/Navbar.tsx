import { Link } from 'react-router-dom'


function Navbar() {

    return (<>
        <header className="flex items-center justify-between h-18 bg-sky-400 text-lg ">
            <div className="mr-0 p-0 ml-25 hover:text-white cursor-pointer"> <Link to="/">Logo</Link></div>
            <nav className="flex gap-4 mr-50 cursor-pointer">
                <Link to="/" className="hover:text-white">Accueil</Link>
                <Link to="/" className="hover:text-white">Actualites </Link>
                <Link to="/login" ><button className="rounded-md border-2 pl-2 pr-2 hover:bg-white hover:text-blue-950">se connecter</button></Link>
            </nav>
        </header>
    </>);
}

export default Navbar

import { Link } from "react-router-dom";

function Footer() {
    return (
        <div className="grid grid-cols-2 bg-stone-400 h-72 items-center text-lg">
            
            <div className="text-center hover:text-white cursor-pointer">
                Logo
            </div>

            <div className="flex flex-col gap-4 items-center border-l border-state-500 h-40 justify-center ">
                <Link to="/" className="hover:text-white cursor-pointer">Accueil</Link>
                <Link to="/" className="hover:text-white cursor-pointer">Actualites</Link>
                <Link to="/login" className="hover:text-white cursor-pointer">Se Connecter</Link>
            </div>

        </div>
    );
}

export default Footer;
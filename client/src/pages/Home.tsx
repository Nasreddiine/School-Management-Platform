import Footer from "@/components/Footer";
import Navbar from "@/components/Navbar";
import { Link } from "react-router-dom";



function Home(){

    return(<>
    <Navbar />
    <div className="min-h-100 bg-[url('/herobgimg.jpg')] bg-cover bg-center">
      <div className="text-lg text-center">Ecole de L'AIR</div>
      <div className="text-lg text-cente">Notre ecole Notre avenir</div>
      <div><Link to="/login">Se Connecter</Link></div>
    </div>
    <Footer />
    </>);
}


export default Home
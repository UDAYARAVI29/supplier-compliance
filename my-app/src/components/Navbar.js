import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <nav>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/suppliers">Suppliers</Link></li>
                <li><Link to="/compliance">Compliance</Link></li>
                <li><Link to="/insights">Insights</Link></li>
            </ul>
        </nav>
    );
};

export default Navbar;

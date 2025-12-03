import React from "react";
import { Outlet, Link } from "react-router-dom";

export const Layout = () => {
    return (
        <>
            <nav className="navbar navbar-light bg-light mb-4 px-3">
                <Link to="/" className="navbar-brand">Inicio</Link>
                <Link to="/demo" className="btn btn-primary">Listas</Link>
            </nav>

            <div>
                <Outlet />
            </div>
        </>
    );
};

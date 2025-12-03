import { useState } from "react";
import { registerUser } from "../services/auth";

export default function Register() {
    const [user, setUser] = useState({ email: "", password: "" });

    const handleSubmit = async e => {
        e.preventDefault();
        await registerUser(user);
    };

    return (
        <div className="container mt-5">
            <h2>Crear cuenta</h2>
            <form onSubmit={handleSubmit}>
                <input className="form-control mb-2" placeholder="Email" onChange={e => setUser({ ...user, email: e.target.value })} />
                <input className="form-control mb-2" type="password" placeholder="Contraseña" onChange={e => setUser({ ...user, password: e.target.value })} />
                <button className="btn btn-success">Registrarme</button>
            </form>
        </div>
    );
}

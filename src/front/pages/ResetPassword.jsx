import { useState } from "react";

export default function ResetPassword() {
    const [email, setEmail] = useState("");

    const handleSubmit = e => {
        e.preventDefault();
        console.log("Enviar email de recuperación:", email);
    };

    return (
        <div className="container mt-5">
            <h2>Restablecer contraseña</h2>
            <form onSubmit={handleSubmit}>
                <input className="form-control mb-2" placeholder="Tu email" onChange={e => setEmail(e.target.value)} />
                <button className="btn btn-warning">Enviar enlace</button>
            </form>
        </div>
    );
}

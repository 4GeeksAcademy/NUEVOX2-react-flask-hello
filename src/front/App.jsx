import React, { useEffect, useState } from "react";

function App() {
    const [message, setMessage] = useState("");

    useEffect(() => {
        fetch("http://127.0.0.1:5000/api/message")
            .then((res) => res.json())
            .then((data) => setMessage(data.msg))
            .catch((err) => console.error(err));
    }, []);

    return (
        <div>
            <h1>React y Flask juntos</h1>
            <p>Mensaje del backend: {message}</p>
        </div>
    );
}

export default App;

import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom/client";

const App = () => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/projects")
      .then(res => res.json())
      .then(data => setProjects(data));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>3D Project Library</h1>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))", gap: 20 }}>
        {projects.map(p => (
          <div key={p.id} style={{ border: "1px solid #ccc", padding: 10, borderRadius: 8 }}>
            <h2>{p.name}</h2>
            <p><strong>Version:</strong> {p.version}</p>
            <p>{p.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);

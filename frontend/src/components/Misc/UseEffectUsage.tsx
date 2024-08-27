import { useEffect, useState } from "react";

const UseEffectUsage = () => {
    const [count, setCount] = useState(0);

    console.count("hello");

    useEffect(() => {
        console.log("mounted");
        const interval = setInterval(() => {
            setCount((prev) => prev + 1);
        }, 1000);

        return () => {
            console.log("unmounted");
            clearInterval(interval);
        };
    }, []);
    return (
        <div className="card">
            <button onClick={() => setCount((count) => count + 1)}>
                count is {count}
            </button>
        </div>
    );
};

export default UseEffectUsage;

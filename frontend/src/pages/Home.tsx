import React from "react";
import CardLayout from "../components/global/CardLayout";

const Home: React.FC = () => {
    const leftFeed = {}
    const centerFeed = {}
    const rightFeed = {}

    return (
        <div>
            <CardLayout leftFeed={leftFeed} centerFeed={centerFeed} rightFeed={rightFeed} />
        </div>

    );
}

export default Home;
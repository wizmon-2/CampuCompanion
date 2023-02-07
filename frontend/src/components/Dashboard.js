import * as React from "react";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Side from "./scenes/global/Side";
import Top from "./scenes/global/Top";

export default function Dashboard() {

    return (
        <div>
            <Top />
            <Side />
        </div>
    );
}
import React from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Dashboard from "./Dashboard";
import SignIn from "./SignIn";

import { ProSidebarProvider } from 'react-pro-sidebar';

export default function App(props) {
	return (
			<Router>
				<Routes>
					<Route path="/" element={<SignIn />} />
					<Route path="/dashboard" element={<ProSidebarProvider><Dashboard /></ProSidebarProvider>} />
				</Routes>
			</Router>
		);
}

const appDiv = document.getElementById('app');
render(<App />, appDiv);
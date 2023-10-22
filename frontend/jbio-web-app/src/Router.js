import {createBrowserRouter, RouterProvider} from "react-router-dom";

import About from './components/About.js';
import OneDE from './components/OneDE.js';
import TwoDE from './components/TwoDE.js';
import Instructions from './components/Instructions.js';
import Contact from './components/Contact.js';

function Router({isOpen}) {
    const router = createBrowserRouter([
      {
        path: "/",
        element: <About />,
      },
      {
        path: "1de",
        element: <OneDE />,
      },
      {
        path: "2de",
        element: <TwoDE />,
      },
      {
        path: "instructions",
        element: <Instructions />,
      },
      {
        path: "contact",
        element: <Contact />,
      },
    ]);
    return (
        <div className={isOpen ? "content" : "content-collapsed"}>
            <RouterProvider router={router} />
        </div>
    );
}

export default Router;
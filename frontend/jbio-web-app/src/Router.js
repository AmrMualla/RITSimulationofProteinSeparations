import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";

import About from './components/About.js';
import Two from './components/Two.js';

function Router() {
    const router = createBrowserRouter([
      {
        path: "/",
        element: <About />,
      },
      {
        path: "two",
        element: <Two />,
      },
    ]);
    return <RouterProvider router={router} />
}

export default Router;
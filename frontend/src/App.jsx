import { createBrowserRouter, RouterProvider } from 'react-router-dom';

import Layout from './components/Layout';
import NewsScreen from './screens/NewsScreen';
import UsersScreen from './screens/UsersScreen';


const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        index: true,
        element: <NewsScreen />,
      },
      {
        path: "/users",
        element: <UsersScreen />,
      }
    ],
  },
])


function App() {
  return (
    <RouterProvider router={router} />
  )
}

export default App;

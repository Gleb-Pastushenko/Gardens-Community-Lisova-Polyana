import { Outlet } from 'react-router-dom'
import { Container } from 'react-bootstrap'

import Header from "./Header"


function Layout() {
  return (
    <>
      <Header />
      <main className="py-3">
        <Container>
          <Outlet />
        </Container>

      </main>
    </>
  )
}

export default Layout

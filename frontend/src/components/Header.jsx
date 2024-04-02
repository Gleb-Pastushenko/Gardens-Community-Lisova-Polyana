import { Container, Navbar, Nav } from 'react-bootstrap'
import { Link } from 'react-router-dom'

const Header = () => {
  return (
    <header>
      <Navbar collapseOnSelect expand="lg" className="bg-body-tertiary">
        <Container>
          <Navbar.Brand href="/">
            <img src="/site-logo.png" alt="site logo" />
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav" collapseOnSelect>
            <Nav className="ms-auto pt-4 pt-lg-0">
              <Nav.Link className="ms-auto" href="#" to="/" as={Link}>Новини</Nav.Link>
              <Nav.Link className="ms-auto" href="#" to="/users" as={Link}>Члени товариства</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </header>
  )
}

export default Header
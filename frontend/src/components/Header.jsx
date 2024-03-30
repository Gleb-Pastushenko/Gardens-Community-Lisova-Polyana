import { Container, Navbar, Nav } from 'react-bootstrap';

const Header = () => {
  return (
    <header>
      <Navbar expand="lg" className="bg-body-tertiary" collapseOnSelect>
        <Container>
          <Navbar.Brand href="/">
            <img src="/site-logo.png" alt="site logo" />
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="ms-auto pt-4 pt-lg-0">
              <Nav.Link className="ms-auto" href="#home">Новини</Nav.Link>
              <Nav.Link className="ms-auto" href="#link">Оголошення</Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </header>
  )
}

export default Header
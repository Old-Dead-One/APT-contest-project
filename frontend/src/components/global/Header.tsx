import React from "react";
import { Link } from "react-router-dom";
import { Navbar, Nav, Container, Row, Col } from "react-bootstrap";
import { FaHome, FaUser, FaUsers, FaShoppingCart, FaSignInAlt, FaSignOutAlt } from "react-icons/fa";
import SearchBar from "./SearchBar";

const Header: React.FC = () => {
    return (
        <Navbar bg="dark" variant="dark" expand="lg" fixed="top">
            <Container fluid>
                <Row className="w-100">
                    <Col xs="auto" className="d-flex">
                        <Navbar.Brand as={Link} to="/">Side Games</Navbar.Brand>
                        <SearchBar />
                    </Col>

                    <Col xs="auto">
                        <Nav>
                            <Nav.Link as={Link} to="/">
                                <FaHome />
                            </Nav.Link>
                        </Nav>
                        <Nav>
                            <Nav.Link as={Link} to="/profile">
                                <FaUsers />
                            </Nav.Link>
                        </Nav>
                        <Nav>
                            <Nav.Link as={Link} to="/login">
                                <FaShoppingCart />
                            </Nav.Link>
                        </Nav>
                    </Col>

                    <Col xs="auto">
                        <Nav>
                            <Nav.Link as={Link} to="/register">
                                <FaUser />
                            </Nav.Link>
                        </Nav>
                        <Nav>
                            <Nav.Link as={Link} to="/login">
                                <FaSignInAlt />
                            </Nav.Link>
                        </Nav>
                        <Nav>
                            <Nav.Link as={Link} to="/logout">
                                <FaSignOutAlt />
                            </Nav.Link>
                        </Nav>
                        <Nav>
                            <Nav.Link as={Link} to="/cart">
                                <FaShoppingCart />
                            </Nav.Link>
                        </Nav>
                    </Col>
                </Row>
            </Container>
        </Navbar >
    );
}

export default Header;
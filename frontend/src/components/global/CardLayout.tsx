import React from "react";
import { Container, Row, Col, Card } from "react-bootstrap";

interface FeedContent {
    leftFeed: any;
    centerFeed: any;
    rightFeed: any;
}

const CardLayout: React.FC<FeedContent> = (props) => {
    return (
        <Container>
            <Row>
                <Col>
                    <Card>
                        <Card.Body>
                            {props.leftFeed}
                        </Card.Body>
                    </Card>
                </Col>
                <Col>
                    <Card>
                        <Card.Body>
                            {props.centerFeed}
                        </Card.Body>
                    </Card>
                </Col>
                <Col>
                    <Card>
                        <Card.Body>
                            {props.rightFeed}
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>
    );
}

export default CardLayout;


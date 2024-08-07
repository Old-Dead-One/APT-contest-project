import React from "react";
import { Container, Row, Col, Card } from "react-bootstrap";


interface LeftFeedProps {
    chapterID: number;
    chapterName: string;
    chapterLocation: string;
}

const LeftFeed: React.FC<LeftFeedProps> = (props) => {
    return (
        <Container>
            <Row>
                <Col>
                    <Card>
                        <Card.Body>
                            <h1>{props.chapterName}</h1>
                            <p>{props.chapterLocation}</p>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>
    );
}

export default LeftFeed;
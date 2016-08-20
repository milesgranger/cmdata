/**
 * Created by milesg on 8/11/16.
 */

var Button = ReactBootstrap.Button;
var Modal = ReactBootstrap.Modal;
var OverlayTrigger = ReactBootstrap.OverlayTrigger;
var Popover = ReactBootstrap.Popover;
var Tooltip = ReactBootstrap.Tooltip;
var Form = ReactBootstrap.Form;
var FormGroup = ReactBootstrap.FormGroup;
var Col = ReactBootstrap.Col;
var Row = ReactBootstrap.Row;
var Grid = ReactBootstrap.Grid;

class ContactForm extends  React.Component {
    constructor(props){
        super(props);
    }

    render () {
        const popover = (
          <Popover id="modal-popover" title="popover">
            very popover. such engagement
          </Popover>
        );
        const tooltip = (
          <Tooltip id="modal-tooltip">
            wow.
          </Tooltip>
        );

        return (
            <div className="row">
                <div className="col-xs-4 col-xs-offset-4">
                <Modal {...this.props} style={{'margin-top': '10%'}}>
                    <Modal.Header closeButton>
                        <Modal.Title>Contact us</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <form>
                            <div className="form-group">
                                <label htmlFor="email">Your email</label>
                                <input name="email" className="form-control" type="email"/>
                            </div>
                            <div className="form-group">
                                <label name="message" htmlFor="message">Message</label>
                                <textarea name="message" rows="5" className="form-control" type="text"/>
                            </div>
                            <div className="form-group text-center">
                                <button type="submit" className="btn btn-primary">Send!</button>
                            </div>
                        </form>
                    </Modal.Body>
                    <Modal.Footer>
                        <Button onClick={this.props.onHide}>Cancel</Button>
                    </Modal.Footer>
                </Modal>
                </div>
                </div>
        )
    }
}


class BusinessAreas extends React.Component {
    constructor(props){
        super(props);
    }

    render (){
        return (
            <Col md={4}>
                <div style={{'min-height':'20%'}} className="well">
                    <i className={this.props.glyph}></i>
                    <h4>{this.props.businessArea}</h4>
                    <button className="btn btn-info">Learn more.</button>
                </div>
            </Col>
        )
    }
}

class Main extends React.Component {

    constructor(props){
        super(props);
        this.successful = false;
        this.state = {view: 'home', serverData: null, showContactForm: false};
    }

    componentDidMount(){
        console.log('Mounted');
        document.getElementById('home-link').addEventListener('click', function(){ this.setState({view: 'home'})}.bind(this));
        document.getElementById('contact-us').addEventListener('click', function(){this.setState({showContactForm: true})}.bind(this));

    }
    componentWillUnmount (){
    }

    componentDidUpdate (){
    }

    contactUs (){

        var close = () => this.setState({showContactForm: false});

        return(
            <ContactForm show={true} onHide={close}  />
        )

    }

    renderHome() {
        return(
                <div className="row">
                    <div className="col-md-12">
                        <div className="well well-md text-center">
                            <h3>There's a lot of data out there.</h3>
                            <h4>Let's make sense of it.</h4>
                            <hr/>
                            <button onClick={() => {
                                return this.setState({view: 'areas'})
                            }} className="btn btn-primary" value="Find out more">Find out more.
                            </button>
                        </div>
                    </div>
                </div>

    )
    }

    renderAreas () {
        return (
            <Grid fluid={true}>
                <Row>
                    <Col md={12} className="text-center">
                        <h3>
                            Areas of specialty
                        </h3>
                        <hr/>
                        </Col>
                </Row>

                <Row className="text-center">
                    <BusinessAreas glyph="glyphicon glyphicon-signal"
                                   businessArea="Statistical Modeling & Prediction"/>
                    <BusinessAreas glyph="glyphicon glyphicon-hdd"
                                   businessArea="Data Management"/>
                    <BusinessAreas glyph="glyphicon glyphicon-list-alt"
                                   businessArea="Custom Reporting"/>
                </Row>
            </Grid>
            )
    }

    render () {

        if (this.state.showContactForm) {
            return this.contactUs();
        }

        else if (this.state.view == 'home'){
            return this.renderHome();
        }
        else if (this.state.view == 'areas'){
            return this.renderAreas();
        }


    } // End of main render funct
}

$(document).ready(function(){

    window.addEventListener('resize', function(){
        var windowHeight = parseInt($(window).height());
        $('#particles-js').css({'height': windowHeight});
    });

    var windowHeight = parseInt($(window).height());
    $('#particles-js').css({'height': windowHeight});


    ReactDOM.render(<Main/>, document.getElementById('app'));

});

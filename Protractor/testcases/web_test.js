//can have multiple suites in one file

describe("S1",function () {
   
   beforeAll(function (){
       console.log("This is beforeall")
   })
    afterAll(function () {
        console.log(" This is afterall")
    })
   
    beforeEach(function () {
       console.log("-> This is beforeeach");
   })
    afterEach(function () {
        console.log("-> This is aftereach");
    })

    it("S1-T1",function () {
        //Steps to run
        console.log("--> S1-T1");
    })

    it("S1-T2", function () {
        //Steps to run
        console.log("--> S1-T2");
    })
})

describe("S2", function () {

    it("S2-T1", function () {
        //Steps to run
        console.log("--> S2-T1");
    })

    it("S2-T2", function () {
        //Steps to run
        console.log("--> S2-T2");
    })
})
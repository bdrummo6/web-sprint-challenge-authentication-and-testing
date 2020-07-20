
const request = require('supertest');
const server = require('../index.js');
const db = require('../database/dbConfig');
const bcrypt = require('bcryptjs');

beforeEach(async () => {
	await db.seed.run();
})

afterAll(async () => {
	await db.destroy();
})

describe('tests for index.js', () => {
	// GET '/' tests
	describe("GET '/' tests", () => {
		it('it has process.env.DB_ENV as "testing"', async () => {
			expect(process.env.DB_ENV).toBe('testing');
		})

		it("GET '/' should return a status code of 200", async () => {
			const expectedStatusCode = 200;

			const res = await request(server).get('/');

			expect(res.status).toEqual(expectedStatusCode);

		});

		it("GET '/' should return the following message", async () => {
			const res = await request(server).get('/');

			expect(res.body.message).toBe('The API is running!');
		});

		it("GET '/' should return a JSON object", async () => {
			const res = await request(server).get('/');

			expect(res.type).toEqual('application/json');
		});
	});

	// GET all users endpoint tests
	describe("GET '/auth/users' tests", () => {
		it("GET '/auth/users' should return a status code of 200", async () => {
			const expectedStatusCode = 200;

			const res = await request(server).get('/auth/users');

			expect(res.status).toEqual(expectedStatusCode);

		});

		it("GET '/auth/users' should return a JSON object", async () => {
			const res = await request(server).get('/auth/users');

			expect(res.type).toEqual('application/json');
		});
	});

	// Test register
	describe("POST '/auth/register' tests", () => {
		it("POST '/auth/register' should return a status code of 201", async () => {
			const expectedStatusCode = 201;

			const res = await request(server).post('/auth/register').send({
				name: 'test-user-05',
				password: bcrypt.hashSync('test-password-05', 14),
				level: 'user'
			});

			expect(res.status).toEqual(expectedStatusCode);

		});

		it("POST '/auth/register' should return a JSON object", async () => {
			const res = await request(server).post('/auth/register').send({
				name: 'test-user-06',
				password: bcrypt.hashSync('test-password-06', 14),
				level: 'user'
			});

			expect(res.type).toEqual('application/json');
		});
	});

	// Test login
	describe("POST '/auth/login' tests", () => {
		it("POST '/auth/register' should return a status code of 201", async () => {
			const expectedStatusCode = 200;

			const res = await request(server).post('/auth/login').send({
				name: 'user-01',
				password: 'password-01',
			});

			expect(res.status).toEqual(expectedStatusCode);

		});

		it("POST '/auth/login' should return a JSON object", async () => {
			const res = await request(server).post('/auth/login').send({
				name: 'user-02',
				password: 'password-02',
			});

			expect(res.type).toEqual('application/json');
		});
	});

	// GET jokes
	describe("GET '/jokes' tests", () => {
		it("GET '/jokes' should return a status code of 200", async () => {
			const expectedStatusCode = 200;

			const res = await request(server).get(`/jokes`);

			expect(res.status).toEqual(expectedStatusCode);

		});

		it("GET '/jokes' should return a JSON object", async () => {

			const res = await request(server).get(`/jokes`);

			expect(res.type).toEqual('application/json');
		});
	});

});
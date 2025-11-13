# Testing Checklist for User Profiles and Post Ownership

## ✅ Pre-Testing Setup

- [x] Migrations created and applied
- [x] Profile model created
- [x] Post model updated with author field
- [x] Signals configured
- [x] Templates created
- [x] URLs configured
- [x] No linting errors
- [x] Django system check passed
- [x] Server starts without errors

## 🧪 Testing Steps

### 1. User Registration & Profile Creation
- [ ] Register a new user account
- [ ] Verify profile is automatically created
- [ ] Check profile page is accessible
- [ ] Verify default values are applied

### 2. Profile Management
- [ ] Navigate to your profile
- [ ] Click "Edit Profile"
- [ ] Update bio, location
- [ ] Upload profile picture
- [ ] Add social media links
- [ ] Save changes
- [ ] Verify changes appear on profile

### 3. Post Creation with Ownership
- [ ] Create a new post while logged in
- [ ] Verify post appears in posts list
- [ ] Verify your username appears as author
- [ ] Check author link goes to your profile
- [ ] Verify Edit/Delete buttons are visible

### 4. Post Ownership Verification
- [ ] Create posts as User A
- [ ] Logout and register User B
- [ ] View User A's posts as User B
- [ ] Verify you CANNOT see Edit/Delete buttons
- [ ] Try accessing edit URL directly (should fail)

### 5. My Posts Page
- [ ] Navigate to "My Posts"
- [ ] Verify only your posts appear
- [ ] Check post count is correct
- [ ] Verify all Edit/Delete buttons work

### 6. Profile Viewing
- [ ] Click on different author names
- [ ] View their profile pages
- [ ] Verify their posts are listed
- [ ] Check bio and profile info displays
- [ ] Verify Edit button only on own profile

### 7. Post List & Detail Pages
- [ ] Check posts list shows authors
- [ ] Click on post to view detail
- [ ] Verify author card displays
- [ ] Check profile picture appears
- [ ] Test author profile link

### 8. Permissions Testing
- [ ] Try editing another user's post
- [ ] Try deleting another user's post
- [ ] Verify proper error messages
- [ ] Check redirects work correctly

### 9. Navigation Testing
- [ ] Verify "My Posts" link appears when logged in
- [ ] Verify "Profile" link appears when logged in
- [ ] Check navigation changes for guests
- [ ] Test all nav links work

### 10. Edge Cases
- [ ] Profile without picture (default shows)
- [ ] Profile without bio (doesn't break)
- [ ] User with no posts (shows "No posts")
- [ ] Empty profile fields (handled gracefully)

## 🔍 Visual Checks

- [ ] Profile pictures display correctly
- [ ] Author names are styled and clickable
- [ ] Edit/Delete buttons have proper styling
- [ ] Profile page layout is responsive
- [ ] Forms are properly styled
- [ ] Messages display correctly
- [ ] Navigation is clear and accessible

## 🐛 Common Issues to Check

1. **Profile not created**:
   - Check signals are registered in apps.py
   - Verify ready() method exists

2. **Cannot edit posts**:
   - Ensure ownership check uses `==` not `=`
   - Verify user is logged in

3. **Profile picture not showing**:
   - Check MEDIA_URL in settings
   - Verify media URLs in main urls.py
   - Check file permissions

4. **Author field error**:
   - Ensure default user (ID=1) exists
   - Check migrations applied

5. **Template errors**:
   - Verify template paths are correct
   - Check template extends layout.html

## 🎯 Success Criteria

All features working when:
- ✅ Users can register and profile auto-creates
- ✅ Users can edit their own profiles
- ✅ Posts show correct author
- ✅ Only owners can edit/delete posts
- ✅ Profile pages display user info and posts
- ✅ Navigation links work for all users
- ✅ Permissions are properly enforced
- ✅ No console errors
- ✅ No server errors
- ✅ Responsive design works

## 📊 Test Results

| Feature | Status | Notes |
|---------|--------|-------|
| User Registration | ⏳ | |
| Auto Profile Creation | ⏳ | |
| Profile Editing | ⏳ | |
| Post Ownership | ⏳ | |
| Edit Permissions | ⏳ | |
| Delete Permissions | ⏳ | |
| Profile Viewing | ⏳ | |
| My Posts Page | ⏳ | |
| Author Display | ⏳ | |
| Navigation | ⏳ | |

Legend:
- ⏳ Not tested yet
- ✅ Working
- ❌ Issues found
- ⚠️ Partial

---

Test with multiple users to ensure proper ownership verification!

